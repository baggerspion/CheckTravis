# CheckTravis
Simple Python script that will scan your Github organisation for instances of .travis.yml.

## Configuration

All configuration is provided within the `app.json` file. There are two
configurations to be provided:

- "githubAccessToken": This is you Github provided access token. You can create
  your token, [here](git@github.com:therealpadams/CheckTravis.git).
- (optional) "endpoint": Provide the URL of your Github Enterprise endpoint
  here, otherwise, if this is not included at all, the script will call the
public Github

## Usage

The CheckTravis script is called like this: `python3 CheckTravis [org_name]`

If `org_name` is specified, the script will only scan the specific
organisation. **Otherwise, the script will attempt to scan all organisations.**
