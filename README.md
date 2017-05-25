[deoplete.nvim](https://github.com/Shougo/deoplete.nvim) source to autocomplete words from the current [Firefox](https://www.mozilla.org/en-US/firefox/new/) tab.

## Requirements

- [Vimperator](http://vimperator.org/)
- [deoplete.nvim](https://github.com/Shougo/deoplete.nvim)

## Why not X

- [marionette_driver](http://marionette-client.readthedocs.io/en/latest/basics.html) will steal focus from vim once you do `client.start_session()` (also it's python 2)
- [Selenium](http://www.seleniumhq.org/) [can't attach to an existing ff session](https://github.com/seleniumhq/selenium-google-code-issue-archive/issues/18).

## Installation

`~/.vimrc`:

```
Plug 'thalesmello/webcomplete.vim'
```

`~/.vimperatorrc`:

```
javascript function save_url(){ var f = new io.File('/dev/shm/ff_current_url',"w"); f.write(buffer.URL); }
javascript function save_words(){ var f = new io.File('/dev/shm/ff_current_words',"w"); f.write(window.content.document.body.textContent.split(/\s+/).sort().filter(function(v,i,o){return (v.length > 3) && v!==o[i-1]}).join("\n")); }
autocmd LocationChange .* :js save_url();save_words();
```

## Notes

- `df -T /dev/shm` should obviously mention that type is [tmpfs](https://en.wikipedia.org/wiki/Tmpfs)
- this path should probably become more easily configurable since it might not be the common denominator accross distros
- we could use `" javascript function save_source(){  var f = new io.File('/dev/shm/ff_current_source', "w"); f.write(window.content.document.documentElement.outerHTML) }` and
  do the words extraction with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) or [NLTK](http://www.nltk.org/)
- we could also do line completions similary to [haya14busa/vim-auto-programming](https://github.com/haya14busa/vim-auto-programming)
- we could also do line completions but only on `<code>` or `<pre>` parts of the webpage
- we shouldn't crash if /dev/shm/*  isn't found

## Credits

- [shougo](https://github.com/shougo)
- [thalesmello](https://github.com/thalesmello)
