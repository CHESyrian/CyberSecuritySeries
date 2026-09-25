# Stage 5: Access Control and Identity

## The Core Question

Once a system exists, the fundamental security question becomes:

> Who (or what) is allowed to do what?

Answering that question requires two related ideas: **identity** and **access control**.

## Identity and Authentication

**Identity** is the claim “I am this person / this system / this service.”

**Authentication** is the process of verifying that claim.

Common ways to authenticate (often used in combination):

| Factor Type | Examples | Everyday Analogy |
|-------------|----------|------------------|
| Something you **know** | Password, PIN, passphrase | Knowing the combination to a lock |
| Something you **have** | Phone, hardware token, smart card | Possessing a physical key |
| Something you **are** | Fingerprint, face, voice | Biometric recognition |

Using more than one type is called **multi-factor authentication (MFA)**. It is significantly stronger than any single factor alone.

## Authorization

After a user (or system) has been authenticated, **authorization** decides what actions they are permitted to perform.

Examples of authorization decisions:
- Can this user read the file?
- Can this user modify the database?
- Can this service talk to that other service?
- Can this administrator change security settings?

## Common Access Control Models (Conceptual)

### Discretionary Access Control (DAC)
The owner of a resource decides who else can access it. Common in personal computers and many file systems.

### Mandatory Access Control (MAC)
Rules are set by a central authority and cannot be overridden by ordinary users. Often used in high-security environments.

### Role-Based Access Control (RBAC)
Permissions are assigned to roles (e.g., “Accountant,” “Help-desk Technician,” “System Administrator”). Users are then assigned to roles. This is extremely common in organizations because it scales well.

### Attribute-Based Access Control (ABAC)
Decisions are based on attributes of the user, the resource, the action, and the environment (time of day, location, etc.). More flexible but more complex.

## The Principle of Least Privilege

One of the most important ideas in security:

> Give each user or system only the minimum permissions needed to perform its legitimate tasks — and nothing more.

This limits the damage that can occur if an account is compromised or a mistake is made.

## Identity Lifecycle

In real organizations, identities are managed over time:

1. **Provisioning** — creating the account and granting initial access
2. **Review / Recertification** — periodically checking that access is still appropriate
3. **Modification** — changing roles or permissions when job duties change
4. **De-provisioning** — removing access when someone leaves or no longer needs it

Failure to manage this lifecycle cleanly is a very common source of risk (former employees retaining access, for example).

## Why This Matters

Most successful attacks eventually involve abusing legitimate credentials or excessive permissions. Strong identity and access management is therefore one of the highest-leverage areas of defense.

---

**Next stage:** How cryptography protects data.