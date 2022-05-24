from wac.ast.nodes import *


def test_single_expr_type_is_comparable():
    a = SingleExprType(int)
    b = SingleExprType(int)

    assert a == b


def test_create_tuple_expr_type():
    i = SingleExprType(int)
    f = SingleExprType(float)

    t = TupleExprType((i, f))

    assert t.type == (i, f)


def test_create_empty_tuple_expr_type():
    t = TupleExprType(())

    assert t.type == ()


def test_compare_tuple_expr_type():
    a = TupleExprType((SingleExprType(int),))
    b = TupleExprType((SingleExprType(int),))

    assert a == b


def test_create_int_expr():
    i = IntExpr(1234)

    assert isinstance(i, Expr)
    assert isinstance(i, IntExpr)
    assert i.rtype == SingleExprType(int)
    assert i.value == 1234


def test_create_bool_expr():
    b = BoolExpr(True)

    assert isinstance(b, Expr)
    assert isinstance(b, BoolExpr)
    assert b.rtype == SingleExprType(bool)
    assert b.value is True


def test_create_str_expr():
    s = StrExpr("hello world")

    assert isinstance(s, Expr)
    assert isinstance(s, StrExpr)
    assert s.rtype == SingleExprType(str)
    assert s.value == "hello world"


def test_create_float_expr():
    f = FloatExpr(3.14)

    assert isinstance(f, Expr)
    assert isinstance(f, FloatExpr)
    assert f.rtype == SingleExprType(float)
    assert f.value == 3.14


def test_create_identifier_expr():
    i = IdentifierExpr(SingleExprType(int), "x")

    assert isinstance(i, Expr)
    assert isinstance(i, IdentifierExpr)
    assert i.rtype == SingleExprType(int)
    assert i.name == "x"


def test_create_tuple_expr():
    i = IntExpr(1234)
    f = FloatExpr(3.14)

    t = TupleExpr.of(i, f)

    assert isinstance(t, TupleExpr)
    assert isinstance(t, Expr)

    assert t.rtype == TupleExprType(
        (SingleExprType(int), SingleExprType(float))
    )
    assert t.values == (i, f)


def test_create_binary_expr():
    lhs = IntExpr(1)
    rhs = IntExpr(2)

    expr = BinaryExpr.of(lhs, BinaryExprOper.ADD, rhs)

    assert isinstance(expr, Expr)
    assert isinstance(expr, BinaryExpr)
    assert expr.rtype == SingleExprType(int)
    assert expr.lhs is lhs
    assert expr.rhs is rhs


def test_create_binary_expr_auto_deduce_bool_type():
    lhs = IntExpr(1)
    rhs = IntExpr(2)

    expr = BinaryExpr.of(lhs, BinaryExprOper.EQUALS, rhs)

    assert expr.rtype == SingleExprType(bool)
    assert expr.lhs is lhs
    assert expr.rhs is rhs


def test_create_unary_expr():
    rhs = IntExpr(1234)
    expr = UnaryExpr.of(UnaryExprOper.NEGATIVE, rhs)

    assert isinstance(expr, Expr)
    assert isinstance(expr, UnaryExpr)
    assert expr.rtype == SingleExprType(int)
    assert expr.rhs is rhs


def test_create_unary_expr_auto_deduce_bool_type():
    rhs = BoolExpr(False)
    expr = UnaryExpr.of(UnaryExprOper.NOT, rhs)

    assert expr.rtype == SingleExprType(bool)
    assert expr.rhs is rhs


def test_create_var_def_stmt():
    expr = IntExpr(1234)

    var = VarDefStmt("x", expr)

    assert isinstance(var, Stmt)
    assert isinstance(var, VarDefStmt)
    assert var.name == "x"
    assert var.expr is expr


def test_create_module_def_stmt():
    stmt = VarDefStmt("x", IntExpr(1234))

    mod = ModuleDefStmt(stmts=(stmt,), name="some_module")

    assert isinstance(mod, Stmt)
    assert isinstance(mod, ModuleDefStmt)
    assert mod.name == "some_module"
    assert mod.stmts == (stmt,)
