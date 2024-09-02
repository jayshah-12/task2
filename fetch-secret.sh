export VAULT_ADDR='http://192.168.3.112:8200'
export VAULT_TOKEN='root'





# Fetch name secret from Vault
name=$(vault kv get -field=name secret/myapp)

# Store the secret in a file
mkdir -p secrets-output  # Ensure the directory exists
echo "NAME=$name" > secrets-output/name.env

chmod 600 secrets-output/name.env

echo "Contents of secrets-output directory:"
ls -l secrets-output

# Debugging: Print the contents of the name file
echo "Contents of name.env:"
cat secrets-output/name.env
