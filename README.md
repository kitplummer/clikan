# clikan: CLI (Personal) Kanban
There has been a little chatter about 'personal' kanban on the tubes lately.  I don't know about the need to hype it as personal, but if you're looking to get your head wrapped around stuff needing to get done - then kanban is a healthy tool.  clik is a super simple command-line utility for tracking tasks following the Japanese Kanban (boarding) style.  clik's core intent is to be easy to use, and to maintain simplicity.

## Installation

$`pip install clikan`

Caveat, I've not tested this on many different targets, or with Python 3.

### Create a `.clikan.yaml` in your $HOME directory

```yaml
---
clikan_data: /Users/kplummer/.clikan.dat
limits:
  todo: 10
  wip: 3
  done: 10
```

* `clikan_data` is the datastore file location.
* `limits:todo` is the max number of items allowed in the todo column, keep this small - you want a smart list, not an ice box of ideas here.
* `limits:wip` is the max number of items allowed in in-progress at a given time.  Context-switching is a farce, focus on one or two tasks at a time.
* `limits:done` is the max number of done items visible, they'll still be stored.  It's good to see a list of done items, for pure psyche.

-- or --

$`clikan configure`

to create a default data file location.

This is where the tool will store the history of files.  It's configurable so you can put the data in a Dropbox or other cloud-watched directory for safe archiving/backing up.

## Usage
The basic usage of clikan breaks down into three basic commands:

### Display

$`clikan display` (alias: d)

### New

$`clikan new --task [task text]` (alias: n)

### Promote

$`clikan promote --id [task id]` (alias: p)

And there are more supporting commands:

### Regress

$`clikan regress --id [task id]`

### Remove

$`clikan remove --id [task id]`

### Configure

$`clikan configure`

## Development

It's Python code.  Fork, fix, and submit a PR - it'd be super appreciated.

Tests?  Um, yeah.

## License

MIT License

Copyright 2017 Kit Plummer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Support

Github Issues
