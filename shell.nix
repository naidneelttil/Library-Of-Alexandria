{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.fastapi
    python3Packages.psycopg2
    python3Packages.flake8
  ];
}
