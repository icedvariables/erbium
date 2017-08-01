import erblexer
import erbparser
import pprint

code = """

/* Assign x to a function that takes a 32-bit signed integer called y and returns a 32-bit signed integer equal to y + 1. */

a = (int32 x, int32 y) -> int32 {
    int32 z = 10
}

int32 b = a(5, 10.5, f)

"""

erblexer.Lexer().build()
p = erbparser.Parser(debug=True)
result = p.parse(code)
pprint.pprint(result)
