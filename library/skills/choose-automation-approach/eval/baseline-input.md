# Baseline input

Use `choose-automation-approach` for this request:

> A six-person bookkeeping firm wants a four-week pilot that reads new messages in a shared support
> Gmail inbox, classifies the request, and prepares a draft reply. About 30 messages arrive each day
> from customers and unknown external senders. A staff member currently reviews and sends each reply;
> the owner may want automatic sending later, but it is not required for the pilot.
>
> The Fellow wants the quickest useful version and does not want to operate new infrastructure. They
> have: (1) a built-in Gmail connector that can read messages and create drafts, (2) a third-party
> hosted MCP that can also send messages after OAuth login, (3) the official Gmail API, which would
> require configuring a Google Cloud OAuth app, and (4) browser access. The Fellow plans to run the
> pilot from their personal agent cloud environment and use a low-cost model for classification.
>
> The Fellow's personal Google account can currently access the shared mailbox. The firm has no secret
> manager and no dedicated automation account. Errors in a draft are easy to catch; sending a wrong
> reply to a customer would be reputationally harmful. The Fellow values build speed first, then easy
> handoff. Give a recommendation now and ask only if a missing fact would materially change it.
