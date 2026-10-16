# AIGoat optional Module 07 role simulation, 16 October 2026

## Scope and personas

This was one maintainer-operated simulation on Windows, not feedback from two independent people. The **student persona, Sam**, is a Module 07 learner who has completed the required BrokenPilot tool lab and wants to try the optional live MCP extension. Sam has Docker Desktop and Ubuntu WSL but has not used AIGoat's interface. The **instructor persona, Riley**, reviews Sam's short journal for evidence and security reasoning. Riley is a course role, not AIGoat's built-in Admin account. No course score, flag, or AIGoat evidence submission is required.

The course checkout was `dev` at `ceb8895`, with the AIGoat v2.0 source pinned to `e1c538badb93c6c1c2307096ab5d709a9ee0fe55`. This host already had the pinned Docker images, WSL source, local configuration, and database. The run checks restart, browser navigation, lab execution, and review. It does **not** measure a first download or build. The accelerated browser walkthrough took roughly four minutes after startup; that is an operator timing, not an estimate for a new learner.

## Student route and observed friction

1. The first launcher attempt stopped because Docker Desktop's engine was not running. After starting Docker Desktop, the same launcher brought up a healthy backend and frontend in about 15 seconds using cached images.
2. The storefront and product images loaded. **Start the Challenges** led to AIGoat's separate CTF. **Try → Attack Labs** and **Console → MCP** initially showed “could not load” messages because the browser had a stale session. The header still offered a generic **User** menu. Logging out and signing in as the documented regular demo user `alice` restored the protected lab lists.
3. The correct route was **Console → MCP**, then the `mcp03-2` and `mcp07-1` lab pages. Each level needed its own **Reset lab**. AIGoat's interaction history carried a previous lab's exchanges until reset, so the reset is also important for a clean journal.
4. The two selected labs completed through the browser without Ollama. The local launcher published only `127.0.0.1:3000`; the backend remained on an internal Docker network, ran as UID/GID `10001`, used a read-only root filesystem, dropped all Linux capabilities, and had `no-new-privileges` set. The live port check also showed a loopback listener for 3000.

## Sam's simulated journal

### MCP03-2, tool redefinition

- **State and actions:** Signed in as regular demo user. At L0, reset, listed Support Server tools, called `lookup_ticket` for `TCK-1008`, listed again, and called the same tool with the same argument. Repeated from reset at L1.
- **Observed evidence:** The first call returned customer-visible ticket status. The later listing changed the description of the same named tool. At L0, the second call returned additional staff fields. At L1, the client displayed a pin mismatch and denied the second call instead of returning those fields.
- **Security explanation:** Approval of a tool name and its earlier description is not lasting authority for a later definition. The client must compare the live tool contract with an approved record before execution. A production broker should also pin schema, server identity, and allowed data scope, then reapprove intentional changes.
- **Residual risk:** Description pinning alone cannot prove that a server implementation still honors its advertised behavior. Server identity, authorization, and result handling remain separate controls.

### MCP07-1, credential passthrough

- **State and actions:** At L0, reset, identified the official Catalog Server and separately maintained Support Server, listed their tools, called support `diagnostics`, and used only the training token shown there with the catalog's mock staff-price tool. At L1, reset and called support `diagnostics` again.
- **Observed evidence:** L0 support diagnostics displayed the catalog-owned decoy credential, and the catalog accepted that copied value for mock staff prices. L1 diagnostics said the catalog credential was not provided to support. The journal intentionally omits the token value and mock staff data.
- **Security explanation:** The client that launches child server processes controls each environment. It should give each integration only its own credentials. Filtering the diagnostics response would hide one symptom while leaving the misplaced credential inside the support process.
- **Residual risk:** A correctly scoped process can still leak its own credential. Audience restriction, short lifetime, rotation, and server-side authorization remain useful.

## Riley's instructor review

**Accept as optional practice evidence, with no grade.** Both entries identify the actor, reset state, repeated call sequence, observation, enforcing control, and residual risk. The second entry separates exposure of the training token from its subsequent use. The first distinguishes the changed listing from the denied call. The source-review path remains available when a learner cannot install Docker.

For a real class, ask the learner to attach a short redacted transcript or screenshot reference for each before/after comparison, then explain in their own words which component made the decision. Do not require upstream flags or scores. This review validates that an instructor can assess the requested journal format; it does not prove a first-time student would complete the route unaided.

## Course fit and remaining gates

Keep AIGoat optional after the required BrokenPilot work. These two cases add MCP tool-contract and credential-distribution boundaries without duplicating BrokenPilot's primary tool-authorization lesson. The Windows guide now names the direct menu path, explicit sign-in, reset sequence, and stale-session recovery. The large initial image build, loosely bounded upstream dependencies, and Windows-only supported launcher remain delivery costs. A fresh independent learner on a clean host and any other operating system still need their own pilot before promising a required or cross-platform live lab.

## Isolated end-to-end follow-up, 16 October 2026

I repeated the course route with a new course checkout at `b5a0f7a58cb506c0795d3b8820f0bb3405065915`, a separate AIGoat source checkout at the pinned `e1c538badb93c6c1c2307096ab5d709a9ee0fe55`, a new ignored local configuration, and a separately named Docker project and database volume. The Windows launcher rebuilt both images from that source. Docker was allowed to reuse cached dependency layers, so this checks a fresh source, configuration, and database on the same host, not a cold build or first-time download. No Ollama service or model was needed. The initial rebuild and start took about 23 seconds on this cached host.

The browser initially displayed the prior generic **User** session state, even against the new database. Following the revised guide, I logged out, signed in as the documented regular demo user `alice`, opened **Console → MCP**, and completed both selected exercises without using AIGoat flags or scores. The fresh-state observations matched the earlier run:

| Exercise | Vulnerable L0 after reset | Protected L1 after reset |
|---|---|---|
| MCP03-2 | A second listing changed `lookup_ticket` from customer-visible status to a full ticket record. The repeated call returned extra staff-only fields. | The initial call returned customer-visible status. After the changed listing, the repeated call was denied with `tool 'lookup_ticket' description does not match the pin`. |
| MCP07-1 | Support diagnostics exposed a catalog-owned training credential. Using that decoy value in the catalog's `staff_prices` tool returned the mock staff price list. | Support diagnostics reported `CATALOG_STAFF_TOKEN: (not provided)`. |

The backend was healthy, had no host port, and ran as UID/GID `10001` with a read-only root filesystem, all Linux capabilities dropped, and `no-new-privileges`. Its only network was the internal lab network. The frontend published `127.0.0.1:3000`, and the Windows listener check also showed only `127.0.0.1`. On the restarted storefront, all 28 visible images had nonzero natural width. These checks cover the tested stack, not every possible container or browser state.

I stopped the isolated stack, confirmed port 3000 closed while its database volume remained, and restarted it without a rebuild. The backend became healthy again in about 11 seconds. Reloading the lab page restored `alice` and stated that earlier exchanges in the attempt remained recorded, although the visible interaction list was empty after reload. I then stopped the stack and confirmed no isolated container or port 3000 listener remained. The test-only source checkouts, ignored configuration, and database volume remain available for reproduction; no lab service is running.

Riley's review remains **acceptable optional practice evidence**. This follow-up increases confidence in the documented Windows learner route and its restart behavior. It is still one maintainer operating both personas on one host with Docker cache. A genuinely independent first-time student, a cold dependency build, and non-Windows delivery have not been validated.
