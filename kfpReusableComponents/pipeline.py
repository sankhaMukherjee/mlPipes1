import os, kfp 

component_root = 'addComp'
add_op = kfp.components.load_component_from_file(os.path.join(component_root, 'component.yaml'))

def pipeline():
    add_task = add_op(
        # Input name "Input 1" is converted to pythonic parameter name "input_1"
        value_1 = '7',
        value_2 = '12',
    )
    # The outputs of the dummy1_task can be referenced using the
    # dummy1_task.outputs dictionary: dummy1_task.outputs['output_1']
    # ! The output names are converted to pythonic ("snake_case") names.

    print(add_task.output)
    print(add_task.outputs['output_1'])

    return

# This pipeline can be compiled, uploaded and submitted for execution.
client = kfp.Client()
client.create_run_from_pipeline_func(pipeline, arguments={})
