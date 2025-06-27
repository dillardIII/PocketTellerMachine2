{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.setuptools
    pkgs.python311Packages.wheel
    pkgs.python311Packages.numpy
    pkgs.ffmpeg
    pkgs.git
    pkgs.portaudio
    pkgs.libpulseaudio
  ];

  env = {
    LD_LIBRARY_PATH = "${pkgs.portaudio}/lib:${pkgs.libpulseaudio}/lib";
    PYTHONPATH = "${pkgs.python311Packages.numpy}/${pkgs.python311.sitePackages}";
    PYTHONNOUSERSITE = "1";
  };
}