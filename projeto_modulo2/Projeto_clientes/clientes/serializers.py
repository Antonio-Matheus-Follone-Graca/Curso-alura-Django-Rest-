from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    # validações por campo
    def  validate_cpf(self, cpf):
        # se  o cpf for diferente de 11 números
        if len(cpf) != 11:
            # exibindo mensagem de erro
            raise serializers.ValidationError("O cpf deve ter 11 dígitos")
        # retornando valor de   cpf 
        return  cpf
    
    def validate_nome(self,nome):
        # caso só existam número no nome
        if not nome.isalpha():
            # exibindo mensagem de erro
            raise serializers.ValidationError("Não includa números neste campo")
        # retornando valor de   nome 
        return  nome

    def validate_rg(self,rg):
        if len(rg)!= 9:
            # exibindo mensagem de erro
            raise serializers.ValidationError("O RG deve ter 9 dígitos")
        # retornando valor de  rg 
        return  rg
    
    def validate_celular(self,celular):
        if len(celular) < 11:
            # exibindo mensagem de erro
            raise serializers.ValidationError("O celular deve ter 11 dígitos")
        # retornando valor de  celular 
        return  celular



    

    
    