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

#### `del <id>`
Deletes a variable.

- `id` is the name of variable to delete

### Types

#### Strings
Strings are the most basic types. A string literal can be defined by wrapping the literal inside
single or double quotes.

#### Undefined
Undefined (`undefined`) is a sentinel type used to represent undefined values. It can be referred to
as simple `undefined`.
