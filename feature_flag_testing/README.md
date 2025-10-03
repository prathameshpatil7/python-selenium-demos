# Automated UI Validation for Feature Flags or A/B Testing

## Scenario
Our team uses feature flags or A/B testing to roll out new UI features to a subset of users. You want to make sure that:

- The new feature is visible only when the flag is enabled.
- The old version still works when the flag is disabled.
- Both versions behave correctly across browsers.

## Selenium work

We can write Selenium tests that:

- Simulate a user with the feature flag enabled (e.g., via a cookie or query param).
- Simulate a user without the feature flag.
- Validate the presence or absence of new UI elements.
- Perform basic interactions to ensure both versions work.



