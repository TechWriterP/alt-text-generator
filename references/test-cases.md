# Example test cases

Use these cases to check behavior. The expected outputs illustrate intent; exact wording may vary if it preserves the same information.

## 1. UI screenshot: relevant state

**Image:** A deployment page showing Production with a green Success badge and version 2.4.1.

**Context:** Verify that the production deployment completed.

**Expected:** `Production deployment for version 2.4.1 has a Success status`

**Avoid:** Listing navigation items, browser controls, or saying "screenshot of."

## 2. UI screenshot: procedure target

**Image:** Settings page with the Notifications toggle turned off.

**Context:** Turn on email notifications.

**Expected:** `Notifications setting with the email notifications toggle turned off`

## 3. Diagram: flow

**Image:** Client sends a request to an API gateway, which routes it to Service A or Service B; both use one database.

**Context:** Request routing architecture.

**Expected:** `The API gateway routes client requests to Service A or Service B, which share a database`

## 4. Chart: trend

**Image:** Line chart where response time falls from 420 ms in January to 180 ms in June.

**Context:** Performance after optimization.

**Expected:** `Average response time decreases from 420 ms in January to 180 ms in June`

## 5. Chart: limit requires another format

**Image:** Dense chart with 12 monthly values across six series.

**Context:** Exact values are needed for an audit.

**Expected behavior:** Summarize the key comparison in `alt_text` and recommend a data table or long description in `note`.

## 6. Product image: task-relevant feature

**Image:** Rear of a router with the reset opening between the power connector and four Ethernet ports.

**Context:** Locate the reset control.

**Expected:** `Reset opening on the router rear panel, between the power connector and four Ethernet ports`

## 7. Decorative image

**Image:** Abstract blue wave beneath the page title.

**Context:** Purely visual page decoration.

**Expected:** Empty `alt_text` with classification `decorative`.

## 8. Missing context

**Image:** Dialog titled Delete environment with Cancel and Delete buttons.

**Context:** None.

**Expected:** `Delete environment confirmation dialog with Cancel and Delete buttons`

## 9. Unsupported inference

**Image:** Dashboard with a red upward arrow next to 12%.

**Context:** None.

**Expected behavior:** Describe the displayed 12% increase without claiming it is good, bad, revenue, or an error.

## 10. Existing alt text review

**Image:** Sign-in dialog with an invalid-password message.

**Existing alt text:** `Screenshot of a dialog box on a computer screen.`

**Expected:** `Sign-in dialog showing an invalid-password error`
