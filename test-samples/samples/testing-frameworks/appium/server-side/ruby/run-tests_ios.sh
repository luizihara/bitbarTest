#!/bin/bash

TEST=${TEST:="ios_sample_spec.rb"} # Name of the test file

##### Cloud testrun dependencies start
echo "Extracting tests.zip..."
unzip tests.zip

## Environment variables setup
export CPATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include
export SCREENSHOT_FOLDER=target/reports/screenshots/

echo "Setting UDID..."
echo "UDID set to ${IOS_UDID}"

echo "Starting Appium ..."
appium -U ${IOS_UDID}  --log-no-colors --log-timestamp --command-timeout 120
ps -ef|grep appium
##### Cloud testrun dependencies end.

## Run the test:
bundle install
echo "Running test ${TEST}"

# Make sure there's no pre-existing `screenshots` files
rm -rf screenshots
bundle exec rspec ${TEST} --format RspecJunitFormatter  --out TEST-all.xml

# Screenshots need to be available at root as directory `screenshots` .
cp -a ${SCREENSHOT_FOLDER}. screenshots/











