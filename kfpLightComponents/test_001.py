# Example copied form the website:

# --------------------------------
# First deploy a kubeflow cluster
# --------------------------------
# https://www.kubeflow.org/docs/components/pipelines/installation/localcluster-deployment/

# --------------------------------
# Then run this ...
# --------------------------------
# https://github.com/kubeflow/pipelines/blob/master/samples/core/lightweight_component/lightweight_component.ipynb
# https://www.kubeflow.org/docs/components/pipelines/sdk/sdk-overview/
import kfp
import kfp.components as comp
import kfp.dsl as dsl

def myAdd(a: float, b: float) -> float:
   return a + b
   
def myMul(a: float, b: float) -> float:
   return a * b

pipelineSpecs = {
      'name'        : 'Calculation pipeline',
      'description' : 'A toy pipeline that performs arithmetic calculations.'
   }

@dsl.pipeline( **pipelineSpecs )
def pipeline(a='7', b='2', c='12'):
   
   op1 = comp.func_to_container_op(myAdd)
   op2 = comp.func_to_container_op(myMul)
   
   containerOp1 = op1(a, 4)
   containerOp2 = op2(containerOp1.output, b)
   containerOp3 = op1(containerOp2.output, c)

   return containerOp3.output

def main():

   #Specify pipeline argument values
   arguments = {'a': '7', 'b': '8'}
   result = kfp.Client().create_run_from_pipeline_func(pipeline, arguments=arguments)
   print(result)
   
   # client = kfp.Client()
   # print( client.list_pipelines() )
   

   return

if __name__ == '__main__':
   print('Starting the run')
   main()
   print('finished the run')
