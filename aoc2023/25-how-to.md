Install GraphViz:

```bash
sudo apt install -y graphviz evince
```

Evince is a pdf viewer for Linux. WSL knows how to render linux GUI windows like Evince.

Use a text editor to convert graph to .dot (aka .gv) format:

```yml
jfg: jgs vvx xfv htz dmh zhl
mbg: rqf cbn
#...
```

This converts to:

```gv
graph G {
    jfg -- {jgs vvx xfv htz dmh zhl};
    mbg -- {rqf cbn};
    #...
}    
```

Run this through GraphViz's `neato`:

```bash
neato -Tpdf -o output.pdf 25.dot
# To view with Linux:
evince output.pdf
# To view with Windows:
explorer.exe output.pdf
```