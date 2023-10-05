if ( $OutputEncoding -ne 'utf-8' )
{
    $OutputEncoding = [Console]::InputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
}
$env:PYTHONUTF8=1
py .\main.py