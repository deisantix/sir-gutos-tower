# convertendo a codificação de caracteres do powershell para
# a exibição correta de letras especiais
if ( $OutputEncoding -ne 'utf-8' )
{
    $OutputEncoding = [Console]::InputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
}
# ativando a variável de ambiente utf8 do python e rodando programa
$env:PYTHONUTF8=1