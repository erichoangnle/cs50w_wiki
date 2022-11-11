# Python
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[33]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[34][35]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[36] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[37]

Python consistently ranks as one of the most popular programming languages.

### History
Python was conceived in the late 1980s[42] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[43] capable of exception handling (from the start plus new capabilities in Python 3.11) and interfacing with the Amoeba operating system.[13] Its implementation began in December 1989.[44] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life", a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[45] In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[46][47]

Python 2.0 was released on 16 October 2000, with many major new features.[48] Python 3.0, released on 3 December 2008, with many of its major features backported to Python 2.6.x[49] and 2.7.x. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.[50]

Python 2.7's end-of-life was initially set for 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[51][52] No further security patches or other improvements will be released for it.[53][54] Currently only 3.7 and later are supported. In 2021, Python 3.9.2 and 3.8.8 were expedited[55] as all versions of Python (including 2.7[56]) had security issues leading to possible remote code execution[57] and web cache poisoning.[58]

In 2022, Python 3.10.4 and 3.9.12 were expedited[59] and 3.8.13, and 3.7.13, because of many security issues.[60] When Python 3.9.13 was released in May 2022, it was announced that the 3.9 series (joining the older series 3.8 and 3.7) will only receive security fixes going forward.[61] On September 7, 2022, four new releases were made due to a potential denial-of-service attack: 3.10.7, 3.9.14, 3.8.14, and 3.7.14

### Design Philosophy and Features
Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of their features support functional programming and aspect-oriented programming (including metaprogramming[65] and metaobjects).[66] Many other paradigms are supported via extensions, including design by contract[67][68] and logic programming.[69]

Python uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management.[70] It uses dynamic name resolution (late binding), which binds method and variable names during program execution.

Its design offers some support for functional programming in the Lisp tradition. It has filter,mapandreduce functions; list comprehensions, dictionaries, sets, and generator expressions.[71] The standard library has two modules (itertools and functools) that implement functional tools borrowed from Haskell and Standard ML.[72]

Its core philosophy is summarized in the document The Zen of Python (PEP 20), which includes aphorisms such as:[73]

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Readability counts.
Rather than building all of its functionality into its core, Python was designed to be highly extensible via modules. This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. Van Rossum's vision of a small core language with a large standard library and easily extensible interpreter stemmed from his frustrations with ABC, which espoused the opposite approach.[42]

Python strives for a simpler, less-cluttered syntax and grammar while giving developers a choice in their coding methodology. In contrast to Perl's "there is more than one way to do it" motto, Python embraces a "there should be one—and preferably only one—obvious way to do it" philosophy.[73] Alex Martelli, a Fellow at the Python Software Foundation and Python book author, wrote: "To describe something as 'clever' is not considered a compliment in the Python culture."[74]

Python's developers strive to avoid premature optimization and reject patches to non-critical parts of the CPython reference implementation that would offer marginal increases in speed at the cost of clarity.[75] When speed is important, a Python programmer can move time-critical functions to extension modules written in languages such as C; or use PyPy, a just-in-time compiler. Cython is also available, which translates a Python script into C and makes direct C-level API calls into the Python interpreter.

Python's developers aim for it to be fun to use. This is reflected in its name—a tribute to the British comedy group Monty Python[76]—and in occasionally playful approaches to tutorials and reference materials, such as examples that refer to spam and eggs (a reference to a Monty Python sketch) instead of the standard foo, and bar.[77][78]

The programming language's name 'Python' came from the BBC Comedy series Monty Python's Flying Circus. Guido van Rossum thought he needed a name that was short, unique, and slightly mysterious, And so, he decided to name the programming language 'Python'.[76]

A common neologism in the Python community is pythonic, which has a wide range of meanings related to program style. "Pythonic" code may use Python idioms well, be natural or show fluency in the language, or conform with Python's minimalist philosophy and emphasis on readability. Code that is difficult to understand or reads like a rough transcription from another programming language is called unpythonic.[79][80]

Python users and admirers, especially those considered knowledgeable or experienced, are often referred to as Pythonistas.
