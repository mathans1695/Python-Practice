formatter = "%r %r %r %r"

print formatter
print formatter % ('1', 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
      "I had this thing.",
	  "That you could type up right.",
	  "But 'i"'t didn"'"t sing.",
	  "So I said goodnight."
)