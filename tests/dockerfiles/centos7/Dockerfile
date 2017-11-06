FROM centos:7

RUN yum update -y && \
    yum install -y \
      python \
			sudo \
		&& yum clean all


CMD ["/usr/sbin/init"]
