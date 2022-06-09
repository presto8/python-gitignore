# python-gitignore

Python module that implements the gitignore specification, v2.36.1.


# API

```
Gitignore(basedir, debug=False)
  .scan() -> automatically find relevant .gitignore files for basedir
  .import(path, basedir) -> import and parse the specified path as a .gitignore file
  .match(path) -> test if path is ignored but current ruleset
  __call__() -> match
```
