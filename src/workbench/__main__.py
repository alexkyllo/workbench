import click

@click.command()
@click.version_option()
def main() -> None:
    print("workbench.")

if __name__ == "__main__":
    main()