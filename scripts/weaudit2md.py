import sys
import json

def get_location_link(location, repo_link, commit):
    return repo_link + (f"/blob/{commit}/" + location["path"] + f"#L{location['startLine']}-L{location['endLine']}").replace("//", "/")

def parse_entry(entry, repo_link, commit):
    entry_text = f"{entry['label']}"
  
    locations = entry["locations"]
    if len(locations) > 1:
        entry_text += "\n"
        for i in range(len(locations)):
            location = locations[i]
            location_link = get_location_link(location, repo_link, commit)
            #entry_text += f"\t{chr(97 + i)}"
            entry_text += f"\t"
            if len(location["description"]) > 0:
                entry_text += f" {location['description']}"
            entry_text += f" ([location]({location_link}))\n"
    else:
        location = locations[0]
        location_link = get_location_link(location, repo_link, commit)
        if len(location["description"]) > 0:
            entry_text += f" {location['description']}"
        entry_text += f" ([location]({location_link}))\n"
  
    return entry_text

weaudit_fpath = sys.argv[1]  

with open(weaudit_fpath, "r") as f:
    content = json.load(f)
    f.close()

repo_link = content["clientRemote"]
if len(sys.argv) > 2:
    link_mode = sys.argv[2]
    if link_mode == "internal":
        repo_link = content["gitRemote"]
    elif link_mode != "client":
        sys.exit("Error: invalid link mode, mode should be 'internal' or 'client'")
    
commit = content["gitSha"]

findings = []
suggestions = []

for entry in content["treeEntries"]:
    if entry["entryType"] == 1 or entry["details"]["severity"] == "Informational":
        suggestions.append(parse_entry(entry, repo_link, commit))
    else:
        findings.append(parse_entry(entry, repo_link, commit))

message = ""

if len(findings) > 0:
    message += "*Findings*\n"
    for i in range(len(findings)):
        # message += f"{i+1}."
        message += f"{findings[i]}"
    message += "\n\n"

if len(suggestions) > 0:
    message += "*Suggestions*\n"
    for i in range(len(suggestions)):
        # message += f"{i+1}."
        message += f"{suggestions[i]}"

print(message)
