from invoke import task

@task
def test(ctx):
	ctx.run("pytest playme/test")

@task
def build(ctx):
    print("Building!")

@task
def clean(ctx):
    print("Cleaning!")