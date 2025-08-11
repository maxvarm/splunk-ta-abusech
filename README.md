# Add-on for AbuseCH

This Splunk add-on contains modular inputs to collect threat intelligence indicators from
AbuseCH MalwareBazaar, URLhaus, and ThreatFox via corresponding APIs.

## Usage

Get your AbuseCH API key [here](https://auth.abuse.ch/), put it in the global app config, select the input, and configure the collection interval. You should see the same data in Splunk as on AbuseCH. The inputs are restricted to disallow a collection interval lower than every 5 minutes to avoid IP blocking.

Also, some inputs have an upper threshold restriction due to AbuseCH limitations. For example, it's impossible to fetch MalwareBazaar reports older than 60 minutes, so the input won't allow you to set a higher interval, as it may result in missing data.

The add-on does not include event types and field extractions, but creates four new sourcetypes for every modular input:

- abusech:malwarebazaar
- abusech:threatfox
- abusech:urlhausurl
- abusech:urlhauspayload
