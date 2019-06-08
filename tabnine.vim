function! coc#source#tabnine#init() abort
  " options of current source
  return {
        \'shortcut': 'T9',
        \'priority': 0,
        \}
endfunction

function! coc#source#tabnine#complete(opt, cb) abort
  let items = [{
        \ "word": "foo"
        \}, {
        \ "word": "bar"
        \}]
  call a:cb(items)
endfunction
