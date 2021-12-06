from invoke import task

@task
def test(ctx):
	ctx.run("pytest tests")

@task
def build(ctx):
    print("Building!")

@task
def install(ctx):
    print("Cleaning!") 