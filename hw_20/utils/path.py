def abs_path_from_project(relative_path: str):
    import hw_20
    from pathlib import Path

    return (
        Path(hw_20.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
