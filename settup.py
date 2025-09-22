import configparser
import urllib.request
import os
import stat

main_url = "https://raw.githubusercontent.com/itdice/Synology-Cloudflare-DDNS/main/cloudflare.php"
main_file = "/usr/syno/bin/ddns/cloudflare.php"
wildcard_url = "https://raw.githubusercontent.com/itdice/Synology-Cloudflare-DDNS/main/cloudflare-wildcard.php"
wildcard_file = "usr/syno/bin/ddns/cloudflare-wildcard.php"

DDNS_name = "Cloudflare"
DDNS_wildcard_name = "Cloudflare-wildcard"
config_file = "etc.deafaults/ddns_provider.conf"

config - configparser.ConfigParser()
config.read(config_file)

# Main DDNS
try:
  config[DDNS_name]
except KeyError:
  config[DDNS_name] = {}

config[DDNS_name]["modulepath"] = main_file
config[DDNS_name]["queryurl"] = "https://www.cloudflare.com"

# Wildcard DDNS
try:
  config[DDNS_wildcard_name]
except KeyError:
  config[DDNS_wildcard_name] = {}

config[DDNS_wildcard_name]["modulepath"] = wildcard_file
config[DDNS_wildcard_name]["queryurl"] = "https://www.cloudflare.com"

# Save
with open(config_file, 'w') as config_target_file:
  config.write(config_target_file)

# Download
urllib.request.urlretrieve(main_url, main_file)
urllib.request.urlretrieve(wildcard_url, wildcard_file)

# Change Policy
os.chmod(main_file, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
os.chmod(wildcard_file, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
