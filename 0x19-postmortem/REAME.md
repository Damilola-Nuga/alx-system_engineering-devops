Postmortem: Outage Due to Database Connection Exhaustion

On October 15, 2023, our web application experienced a 2-hour outage caused by database connection exhaustion. This postmortem outlines the timeline, root cause, resolution, and steps we’re taking to prevent similar incidents in the future.

![Technical Issue Resolution](./postmorterm_technical.webp)

Issue Summary
Outage Duration: 3:00 PM to 5:00 PM WAT (West African Time).
Impact:
1. 95% of users were unable to access the application.
2. Users experienced slow page loads, followed by “502 Bad Gateway” errors.
3. API requests failed, disrupting both frontend functionality and third-party integrations.
Root Cause: The database connection pool was exhausted due to a misconfigured connection limit and a sudden spike in traffic.

Timeline of Events
Here’s a breakdown of how the incident unfolded:
3:00 PM WAT: Monitoring tools alerted the team to a spike in database connection errors.
3:05 PM WAT: The engineering team was notified via Slack and PagerDuty. Initial assumption: server overload.
3:10 PM WAT: Investigated server logs and CPU/memory usage. No abnormalities were found.
3:20 PM WAT: Application logs revealed a high number of “too many connections” errors from the database.
3:30 PM WAT: Misleading path: The database server was restarted, but the issue persisted.
3:45 PM WAT: The incident was escalated to the DevOps team to investigate database configuration.
4:00 PM WAT: Root cause identified: The database connection pool limit was too low for the current traffic.
4:30 PM WAT: Increased the connection pool limit and optimized slow-running queries.
5:00 PM WAT: Confirmed resolution. Monitoring showed normal database connections, and the application was fully restored.

Root Cause and Resolution
what went wrong?
The database connection pool was configured with a maximum of 50 connections, which was insufficient to handle the sudden spike in traffic caused by a marketing campaign. As a result, the pool was exhausted, and new requests were unable to establish connections, leading to application errors.
How Was It Fixed?
1. Increased the database connection pool limit from 50 to 200 to accommodate higher traffic.
2. Optimized slow-running database queries to reduce connection hold times.
3. Restarted the application server to apply the new configuration.

Corrective and Preventative Measures
To prevent similar incidents in the future, the following measures will be implemented:
Improvements:
1. Regularly review and adjust database connection limits based on traffic trends.
2. Implement auto-scaling for the database connection pool during traffic spikes.
3. Add better monitoring for database connection usage and query performance.
TODO List:
1. Patch the application server to dynamically adjust connection pool limits.
2. Add a monitoring dashboard for database connections and query performance.
3. Conduct load testing to identify the optimal connection pool size.
4. Document a runbook for troubleshooting database connection issues.