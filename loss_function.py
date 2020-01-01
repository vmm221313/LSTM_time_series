def weighted_logsumexp(x,w, dim=None, keepdim=False):
    if dim is None:
        x, dim = x.view(-1), 0
    xm, _ = torch.max(x, dim, keepdim=True)
    x = torch.where(
        # to prevent nasty nan's
        (xm == float('inf')) | (xm == float('-inf')),
        xm,
        xm + torch.log(torch.sum(torch.exp(x - xm)*w, dim, keepdim=True)))
    return x if keepdim else x.squeeze(dim)


def mdn_loss_stable(y,pi,mu,sigma):
    m = torch.distributions.Normal(loc=mu, scale=sigma)
    m_lp_y = m.log_prob(y)
    loss = -weighted_logsumexp(m_lp_y,pi,dim=2)
    return loss.mean()


