import os, kfp 

component_root = 'downloadMNISTComp'
download_op = kfp.components.load_component_from_file(os.path.join(component_root, 'component_dl.yaml'))
extract_op  = kfp.components.load_component_from_file(os.path.join(component_root, 'component_extract.yaml'))
toNpy_op    = kfp.components.load_component_from_file(os.path.join(component_root, 'component_toNpy.yaml'))

def pipeline():

    urls = [
        'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz',
        'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz',
        'http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz',
        'http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz',
    ]

    dlTasks = []
    exTasks = []
    npyTasks = []

    for u in urls:
        dlTask.append( 
            download_op(
                url = u
            )
        )

    for dlTaks in dlTakss:
        exTasks.append(
            extract_op(
                file = dlTask.output
            )
        )
    
    for exTaks in exTakss:
        npyTasks.append(
            toNpy_op(
                file = exTask.output
            )
        )

    
    return

# This pipeline can be compiled, uploaded and submitted for execution.
client = kfp.Client()
client.create_run_from_pipeline_func(pipeline, arguments={})
