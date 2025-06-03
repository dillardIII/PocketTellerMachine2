{ pkgs }: {
  deps = [
    pkgs.vercel-pkg
    pkgs.temurin-bin-17
    pkgs.try
    pkgs.mailutils
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.setuptools
    pkgs.python311Packages.wheel
    pkgs.cairo
    pkgs.ffmpeg-full
    pkgs.freetype
    pkgs.ghostscript
    pkgs.gobject-introspection
    pkgs.gtk3
    pkgs.pkg-config
    pkgs.qhull
    pkgs.tcl
    pkgs.tk
  ];
}