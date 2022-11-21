import cx_Freeze

executables = [cx_Freeze.Executable(
    script="chickenRoad.py",
    icon="assets/logo.png"
)]
cx_Freeze.setup(
    name="ChickenRoad",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }}
    ,executables = executables
)

