# reg ::= rsp | rbp | rax | rbx | rcx | rdx | rsi | rdi |
# r8 | r9 | r10 | r11 | r12 | r13 | r14 | r15
# arg ::= $int | %reg | int(%reg)
# instr ::= addq arg,arg | subq arg,arg | negq arg | movq arg,arg |
# callq label | pushq arg | popq arg | retq | jmp label

from dataclasses import dataclass
from typing import List, Set, Dict, Tuple, Any
from .base_ast import AST

# arg
@dataclass(frozen=True, eq=True)
class Arg(AST):
    pass

@dataclass(frozen=True, eq=True)
class Immediate(Arg):
    val: int

@dataclass(frozen=True, eq=True)
class Reg(Arg):
    val: str

@dataclass(frozen=True, eq=True)
class ByteReg(Arg):
    val: str

@dataclass(frozen=True, eq=True)
class Var(Arg):
    var: str

@dataclass(frozen=True, eq=True)
class VecVar(Var):
    var: str

@dataclass(frozen=True, eq=True)
class GlobalVal(Arg):
    val: str

@dataclass(frozen=True, eq=True)
class FunRef(Arg):
    label: str

@dataclass(frozen=True, eq=True)
class Deref(Arg):
    reg: str
    offset: int

# instr
@dataclass(frozen=True, eq=True)
class Instr(AST):
    pass

@dataclass(frozen=True, eq=True)
class NamedInstr(Instr):
    instr: str
    args: List[Arg]

@dataclass(frozen=True, eq=True)
class Callq(Instr):
    label: str

@dataclass(frozen=True, eq=True)
class IndirectCallq(Instr):
    e1: Arg
    num_args: int

@dataclass(frozen=True, eq=True)
class TailJmp(Instr):
    e1: Arg
    num_args: int

@dataclass(frozen=True, eq=True)
class Jmp(Instr):
    label: str

@dataclass(frozen=True, eq=True)
class JmpIf(Instr):
    cc: str
    label: str

@dataclass(frozen=True, eq=True)
class Set(Instr):
    cc: str
    e1: Arg

@dataclass(frozen=True, eq=True)
class Retq(Instr):
    pass

@dataclass(frozen=True, eq=True)
class Program(AST):
    blocks: Dict[str, List[Instr]]
