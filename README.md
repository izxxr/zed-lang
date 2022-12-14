# zed-lang
An simple and experimental programming language written in Python 3.

## Roadmap
- [x] `print` statement
- [ ] Variables
    - [x] `let` statement
    - [ ] `const` statement (MAYBE)
    - [x] `del` statement
- [ ] Literals
    - [x] Strings
    - [ ] Integers
    - [ ] Booleans
    - [ ] Floats
    - [x] Undefined
- [ ] Control structures
    - [ ] Conditionals
    - [ ] Loops

If you have an idea, open an issue or submit a pull request to add it on this roadmap.

## Installation and usage
The language is written in pure Python and that's why is easy to install and use. Simple
clone this repository and use `python -m zed <filename>` command to run a `.zed` file.

```
$ git clone https://github.com/nerdguyahmad/zed-lang
$ cd zed-lang
$ python -m zed test.zed
```

## Documentation
Following is the documentation that documents current state of the language. This will be
moved to a separate section when it gets big enough to get out of hand.

### Statements
Statements are often referred as keywords. Each statement may or may not take one or more
operands. For example, in `print "Hello"`, `print` is the statement and `"Hello"` is the operand.

#### `print <expr>`
Prints the `expr` to the output.

- `expr` can be anything printable such as a string literal or identifier.

#### `let <id> = <value>` // `let <id>`
Defines a new variable.

- `id` is the name of variable
- When a value is specified e.g `let a = 1`, the variable `a` gets the value of `1`
- When a value is NOT specified e.g `let a`, the variable `a` is defaulted to `undefined` sentinel

For example:
```
let a = 'Hello World'
let c
print a
print c
```
The output is:
```
Hello World
undefined
```

#### `del <id>`
Deletes a variable.

- `id` is the name of variable to delete

For example:
```
let a = 'Hello World'
print a
del a
print a
```
The output is:
```
Hello World
On line 4, column 8, position 6:
error: identifer 'a' is not defined
```

### Types

#### Strings
Strings are the most basic types. A string literal can be defined by wrapping the literal inside
single or double quotes.

#### Undefined
Undefined (`undefined`) is a sentinel type used to represent undefined values. It can be referred to
as simple `undefined`.
