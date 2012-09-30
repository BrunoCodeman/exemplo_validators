# coding: utf8
# try something like
def index():
    response.view = 'funcionario/novo.html' 
    return dict()
    
def novo():
    empresa = db.empresas._filter_fields(request.post_vars)
    funcionario = db.funcionarios._filter_fields(request.post_vars)
    empresa_has_errors  = db.empresas._validate(**empresa)
    funcionario_has_errors = db.funcionarios._validate(**funcionario)
    if not empresa_has_errors and not funcionario_has_errors:
        id_empresa = db.empresas.insert(**empresa)
        funcionario["empresa"] = id_empresa
        db.funcionarios.insert(**funcionario)
        response.flash = 'dados salvos com sucesso!'
    else:
        erros = dict(empresa_has_errors.items() + funcionario_has_errors.items())
        msg_erro = 'os seguintes erros foram encontrados: '
        for k,v in erros.items():
            msg_erro+= v +'. '
        response.flash = str(empresa_has_errors.__class__)#msg_erro
    response.view = 'funcionario/novo.html' 
    return dict()
