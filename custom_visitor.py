from grammar.alexerVisitor import alexerVisitor
from grammar.alexerParser import alexerParser
from ast_nodes import *
class CustomASTVisitor(alexerVisitor):
    def visitProgram(self, ctx: alexerParser.ProgramContext):
        statements = [self.visit(stmt) for stmt in ctx.statement()]
        return ProgramNode(statements)

    def visitStatement(self, ctx: alexerParser.StatementContext):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        elif ctx.assignStmt():
            return self.visit(ctx.assignStmt())
        elif ctx.printStmt():
            return self.visit(ctx.printStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        elif ctx.exprStmt():
            return self.visit(ctx.exprStmt())

    def visitBlock(self, ctx: alexerParser.BlockContext):
        statements = [self.visit(stmt) for stmt in ctx.statement()]
        return BlockNode(statements)

    def visitAssignStmt(self, ctx: alexerParser.AssignStmtContext):
        name = ctx.ID().getText()
        value_node = self.visit(ctx.expr())
        return AssignNode(name=name, value=value_node)

    def visitPrintStmt(self, ctx: alexerParser.PrintStmtContext):
        value_node = self.visit(ctx.expr())
        return PrintNode(value=value_node)

    def visitIfStmt(self, ctx: alexerParser.IfStmtContext):
        condition = self.visit(ctx.expr())
        then_block = self.visit(ctx.block(0))
        else_block = None
        if ctx.block(1):
            else_block = self.visit(ctx.block(1))

        return IfNode(condition=condition, then_block=then_block, else_block=else_block)

    def visitWhileStmt(self, ctx: alexerParser.WhileStmtContext):
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.block())
        return WhileNode(condition=condition, body=body)

    def visitVarDecl(self, ctx: alexerParser.VarDeclContext):
        name = ctx.ID().getText()
        var_type = ctx.type_().getText()
        value_node = self.visit(ctx.expr())
        return VarDeclNode(name=name, var_type=var_type, value=value_node)

    def visitExpr(self, ctx: alexerParser.ExprContext):
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == "(":
                return self.visit(ctx.expr(0))
            left = self.visit(ctx.expr(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expr(1))
            return BinOpNode(left=left, op=op, right=right)
        elif ctx.getChildCount() == 1:
            if ctx.NUMBER():
                return NumberNode(value=float(ctx.NUMBER().getText()))
            elif ctx.ID():
                return IdNode(name=ctx.ID().getText())  