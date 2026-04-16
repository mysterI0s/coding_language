from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass(kw_only=True)
class ASTNode(ABC):
    line: int = 0
    column: int = 0

    @abstractmethod
    def accept(self, visitor: "ASTVisitor"):
        pass


@dataclass
class NumberNode(ASTNode):
    value: float

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_NumberNode(self)


@dataclass
class IdNode(ASTNode):
    name: str

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_IdNode(self)


@dataclass
class BinOpNode(ASTNode):
    left: ASTNode
    op: str
    right: ASTNode

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_BinOpNode(self)


@dataclass
class VarDeclNode(ASTNode):
    name: str
    var_type: str
    value: ASTNode

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_VarDeclNode(self)


@dataclass
class ProgramNode(ASTNode):
    statements: List[ASTNode]

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_ProgramNode(self)


@dataclass
class AssignNode(ASTNode):
    name: str
    value: ASTNode

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_AssignNode(self)


@dataclass
class PrintNode(ASTNode):
    value: ASTNode

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_PrintNode(self)


@dataclass
class BlockNode(ASTNode):
    statements: List[ASTNode]

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_BlockNode(self)


@dataclass
class IfNode(ASTNode):
    condition: ASTNode
    then_block: BlockNode
    else_block: Optional["BlockNode"] = None

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_IfNode(self)


@dataclass
class WhileNode(ASTNode):
    condition: ASTNode
    body: BlockNode

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_WhileNode(self)


class ASTVisitor(ABC):
    @abstractmethod
    def visit_NumberNode(self, node: NumberNode):
        pass

    @abstractmethod
    def visit_IdNode(self, node: IdNode):
        pass

    @abstractmethod
    def visit_BinOpNode(self, node: BinOpNode):
        pass

    @abstractmethod
    def visit_VarDeclNode(self, node: VarDeclNode):
        pass

    @abstractmethod
    def visit_ProgramNode(self, node: ProgramNode):
        pass

    @abstractmethod
    def visit_AssignNode(self, node: AssignNode):
        pass

    @abstractmethod
    def visit_PrintNode(self, node: PrintNode):
        pass

    @abstractmethod
    def visit_BlockNode(self, node: BlockNode):
        pass

    @abstractmethod
    def visit_IfNode(self, node: IfNode):
        pass

    @abstractmethod
    def visit_WhileNode(self, node: WhileNode):
        pass
