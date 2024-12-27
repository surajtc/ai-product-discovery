{pkgs ? import <nixpkgs> {}}:
(pkgs.buildFHSEnv {
  name = "python-env";
  targetPkgs = pkgs:
    with pkgs; [
      python3
      gcc

      which
    ];
  runScript = "zsh";
})
.env
