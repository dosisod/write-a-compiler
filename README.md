# Write a Compiler

Code for my [Write a Compiler](https://dosisod.com/blog/writing-a-compiler-0.html)
blog series.

## Running

Basic setup:

```
$ python3 -m virtualenv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
```

## Testing

Install extra developer dependencies:

```
$ pip3 install -r dev-requirements.txt
```

Run all tests:

```
$ make test
```

## Setting up `pre-commit`

The `pre-commit` file is designed to be ran before each git commit. It is not
enabled by default (for security reasons), so to enable it, run the following:

```
$ ln -sf $PWD/pre-commit .git/hooks/pre-commit
```
