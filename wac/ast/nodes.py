from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Tuple


class Node:
    pass


class ExprType:
    pass


@dataclass
class SingleExprType(ExprType):
    type: type


@dataclass
class TupleExprType(ExprType):
    type: Tuple[ExprType, ...]


@dataclass
class Expr(Node):
    rtype: ExprType = field(init=False)


@dataclass
class IntExpr(Expr):
    rtype = SingleExprType(int)
    value: int


@dataclass
class BoolExpr(Expr):
    rtype = SingleExprType(bool)
    value: bool


@dataclass
class FloatExpr(Expr):
    rtype = SingleExprType(float)
    value: float


@dataclass
class StrExpr(Expr):
    value: str
    rtype = SingleExprType(str)


@dataclass
class IdentifierExpr(Expr):
    rtype: ExprType = field(init=True)
    name: str


@dataclass
class TupleExpr(Expr):
    rtype: TupleExprType = field(init=True)
    values: Tuple[Expr, ...]

    @classmethod
    def of(cls, *args: Expr) -> TupleExpr:
        return cls(
            TupleExprType(tuple(expr.rtype for expr in args)),
            args,
        )


class BinaryExprOper(Enum):
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    POWER = auto()
    EQUALS = auto()
    LESS_THEN = auto()
    LESS_THEN_EQ = auto()
    GREATER_THEN = auto()
    GREATER_THEN_EQ = auto()

    def is_bool_like(self) -> bool:
        oper = type(self)

        return self in (
            oper.EQUALS,
            oper.LESS_THEN,
            oper.LESS_THEN_EQ,
            oper.GREATER_THEN,
            oper.GREATER_THEN_EQ,
        )


@dataclass
class BinaryExpr(Expr):
    rtype: ExprType = field(init=True)
    lhs: Expr
    oper: BinaryExprOper
    rhs: Expr

    @classmethod
    def of(cls, lhs: Expr, oper: BinaryExprOper, rhs: Expr) -> BinaryExpr:
        type = SingleExprType(bool) if oper.is_bool_like() else lhs.rtype

        return cls(type, lhs, oper, rhs)


class UnaryExprOper(Enum):
    NEGATIVE = auto()
    NOT = auto()

    def is_bool_like(self) -> bool:
        return self is type(self).NOT


@dataclass
class UnaryExpr(Expr):
    rtype: ExprType = field(init=True)
    oper: UnaryExprOper
    rhs: Expr

    @classmethod
    def of(cls, oper: UnaryExprOper, rhs: Expr) -> UnaryExpr:
        type = SingleExprType(bool) if oper.is_bool_like() else rhs.rtype

        return cls(type, oper, rhs)


class Stmt(Node):
    pass


@dataclass
class VarDefStmt(Stmt):
    name: str
    expr: Expr


@dataclass
class ModuleDefStmt(Stmt):
    name: str
    stmts: Tuple[Stmt, ...]
