#Python Program using list and its methods.
l1 = [1, 2, 3, 4, 5]
l2 = [48,"Satyam",95]
l3 = ["c", "c++", "java", "python", "javascript", "html", "css", "php", "sql", "ruby", "swift", "kotlin", "go", "rust", "perl", "scala", "typescript", "dart", "lua", "haskell", "elixir", "clojure", "f#", "erlang", "r", "matlab", "groovy", "objective-c", "assembly", "fortran", "cobol", "lisp", "prolog", "smalltalk", "ada", "bash", "powershell", "visual basic", "delphi", "vhdl", "verilog", "julia", "crystal", "nim", "zig", "ocaml", "elm", "reason", "rebol", "factor", "forth", "postscript", "awk", "sed", "tcl", "racket", "scheme", "common lisp", "newlisp", "logo", "scratch", "alice", "snap!", "kodu", "stencyl", "game maker language", "gml", "construct 2", "construct 3", "unreal engine blueprints", "unity c#", "godot gdscript", "cryengine flowgraph", "amazon lumberyard scriptcanvas", "blender python", "maya mel", "houdini vex", "nuke python", "fusion lua", "after effects expressions", "premiere pro extensions", "audition scripts", "photoshop scripts", "illustrator scripts", "indesign scripts", "lightroom plugins", "bridge scripts", "dreamweaver extensions"]
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l1,type(l1))
print(l2,type(l2))
print(l3,type(l3))
print(l4,type(l4))

#list methods
#indexing
print(l1[0])
print(l2[1])
print(l3[2])
print(l4[3])
print(l3[1:7:2])
print(l4[::2])


#methods
l1.append(6)
print(l1)
l3.remove("c++")
print(l3)
l1.extend(l4)
print(l1)
print(l3.count("python"))
print(l3.index("ada"))
print(l4.pop())
print(l4)
l3.sort()
print(l3)
l3.reverse()
print(l3)
l3.remove("python")
print(l3)


#END