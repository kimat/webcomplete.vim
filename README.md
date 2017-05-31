[deoplete.nvim](https://github.com/Shougo/deoplete.nvim) source to autocomplete words from the current [Firefox](https://www.mozilla.org/en-US/firefox/new/) tab.

## Requirements

- [Vimperator](http://vimperator.org/)
- [deoplete.nvim](https://github.com/Shougo/deoplete.nvim)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

## Why not X

- [marionette_driver](http://marionette-client.readthedocs.io/en/latest/basics.html) will steal focus from vim once you do `client.start_session()` (also it's python 2)
- [Selenium](http://www.seleniumhq.org/) can't [attach to an existing ff session](https://github.com/seleniumhq/selenium-google-code-issue-archive/issues/18).

## Installation

`~/.vimrc`:

```
Plug 'https://github.com/kimat/webcomplete.vim.git'
```

`~/.vimperatorrc`:

```
javascript function save_url(){ var f = new io.File('/dev/shm/ff_current_url',"w"); f.write(buffer.URL); }
javascript function save_source(){  var f = new io.File('/dev/shm/ff_current_source', "w"); f.write(window.content.document.documentElement.outerHTML) }
autocmd PageLoad .* :js save_url();save_source();
autocmd LocationChange .* :js save_url();save_source();
```

``



## Notes

- `df -T /dev/shm` should obviously mention that type is [tmpfs](https://en.wikipedia.org/wiki/Tmpfs)
- this path should probably become more easily configurable since it might not be the common denominator accross distros
- we could also do line completions similary to [haya14busa/vim-auto-programming](https://github.com/haya14busa/vim-auto-programming)
- we could also do line completions but only on `<code>` or `<pre>` parts of the webpage
- we shouldn't crash if /dev/shm/*  isn't found
- this could become a languageServer 

## Credits

- [shougo](https://github.com/shougo)
- [thalesmello](https://github.com/thalesmello)
