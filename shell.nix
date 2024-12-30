{pkgs ? import <nixpkgs> {}}:
(pkgs.buildFHSEnv {
  name = "python-env";
  targetPkgs = pkgs:
    with pkgs; [
      python3
      uv
      gcc

      which
    ];
  runScript = "zsh";
})
.env
