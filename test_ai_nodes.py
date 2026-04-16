from ast_nodes import *

dummy_condition = BinOpNode(left=None, op=">", right=None)
dummy_then = BlockNode(statements=[])
if_node = IfNode(condition=dummy_condition, then_block=dummy_then, 
else_block=None)
print("تم إنشاء عقدة الذكاء الصناعي بنجاح!")
print(if_node)