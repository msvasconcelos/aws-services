# Projeto de Estudos AWS Lambda com Python

Este projeto tem como objetivo fornecer um exemplo básico de como usar o AWS Lambda com Python. O AWS Lambda é um serviço de computação sem servidor oferecido pela Amazon Web Services (AWS), que permite executar código sem precisar provisionar ou gerenciar servidores.

No lambda_function recebe um evento com nome, email e cpf e grava no DynamoDB
No lambda_save_s3 recebe um evento e grava no S3 

## Estrutura do Projeto

- `lambda_function.py`: Arquivo com o código da função Lambda que salva no Dynamo.
- `lambda_save_s3.py`: Arquivo com o código da função Lambda que arquiva no s3.
- `lambda_send_sms.py`: Arquivo com o código da função Lambda que envia msg SMS.
- `myevent.json`: Arquivo com exemplo de evento teste para envio no lambda lambda_function
- `myeventsns.json`: Arquivo com exemplo de evento teste para envio no SNS
- `myevents3.json`: Arquivo com exemplo de evento teste para armazenar no S3
- `README.md`: Documentação do projeto.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Basta fazer um fork do repositório, realizar suas alterações e enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.

## Recursos Adicionais

- [Curso AWS: SNS + SQS + LAMBDA + S3 + Python](https://www.youtube.com/playlist?list=PLtyCzf24Ov40hAgIfHohNcOIy8jo0IQ2h)
- [Documentação do AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Documentação do AWS CLI](https://aws.amazon.com/cli/)
- [Documentação do Python](https://docs.python.org/)

Espero que este README tenha sido útil para começar seus estudos com o AWS Lambda e Python. Divirta-se explorando o poder da computação sem servidor!
