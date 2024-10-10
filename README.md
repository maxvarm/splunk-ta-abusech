# Add-on for AbuseCH

This Splunk add-on contains modular inputs to collect threat intelligence indicators from
AbuseCH MalwareBazaar, URLhaus, and ThreatFox via corresponding APIs.

## Usage

Just create an input for the required AbuseCH platform, configure collection interval,
and you should see the same data in Splunk as on the [AbuseCH](https://abuse.ch/).
The APIs do not require any credentials, but inputs are restricted to disallow collection
interval lower than every 5 minutes to avoid IP blocking.

Also, some inputs have upper threshold restriction due to AbuseCH limitations. For example,
it's impossible to fetch MalwareBazaar alerts older than 60 minutes, so the input won't allow
you to set higher interval as it may result in missing data.

The add-on does not include any event types or field extrations, but creates four new
sourcetypes, for every modular input:

-   abusech:malwarebazaar
-   abusech:threatfox
-   abusech:urlhausurl
-   abusech:urlhauspayload
