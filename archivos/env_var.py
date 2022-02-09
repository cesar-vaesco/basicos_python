import os

stage = os.getenv('STAGE', 'dev').upper()

output = 'Corriendo en ambiente de {0}'.format(stage)
#output = f'Mi nombre es: {0}'.format(stage)

if stage.startswith('PROD'):
    output = "DANGER!!! - " + output

print(output)

# STAGE=staging python archivos/env_var.py  
# STAGE=production python archivos/env_var.py 